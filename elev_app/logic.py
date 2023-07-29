from django.db.models import F, Max
from .models import ElevatorModel, RequestModel
from math import inf

#assigning elevators to the floors based on the direction(stopped or same direction)


class ElevatorSystem:

    def __init__(self, num_elevators):
        self.elevators = []
        for i in range(1, num_elevators + 1):
            elevator = ElevatorModel(elev_id=i)
            elevator.save()
            self.elevators.append(elevator)

    def assign_elevator_to_floor(self, floor, direction):
        available_elevators = ElevatorModel.objects.filter(
            elev_working=True, elev_direction__in=['Stopped', direction]
        )

        if not available_elevators:
            return None

        minimum_distance = float('inf')
        best_elevator = None

        for elevator in available_elevators:
            distance = abs(elevator.current_floor - floor)
            if distance < minimum_distance:
                minimum_distance = distance
                best_elevator = elevator

        if best_elevator:
            best_elevator.elev_direction = self.move_elevator(best_elevator, floor)
            best_elevator.save()

            # Update the assigned elevator's current floor to the destination floor
            best_elevator.current_floor = floor
            best_elevator.save()

            RequestModel.objects.create(
                current_floor=floor, floor_direction=direction, destination_floor=None
            )

            # Return the assigned elevator's ID for user feedback
            return best_elevator.elev_id

        return None

    def maintain_elevator(self, elev_id):
        elevator = ElevatorModel.objects.get(elev_id=elev_id)
        elevator.elev_working = False
        elevator.save()

    def open_elevator_door(self, elev_id):
        elevator = ElevatorModel.objects.get(elev_id=elev_id)
        elevator.is_door_open = True
        elevator.save()

    def close_elevator_door(self, elev_id):
        elevator = ElevatorModel.objects.get(elev_id=elev_id)
        elevator.is_door_open = False
        elevator.save()


    def move_elevator(elevator, floor):
        if floor == elevator.current_floor:
            return "Stopped"
        elif floor > elevator.current_floor:
            return "Up"
        else:
            return "Down"
    

def manage_requests(self, elevator):
    requests = RequestModel.objects.filter(
        current_floor=elevator.current_floor, direction=elevator.elev_direction)

    if requests.exists():  # Check if there are requests for the current floor and direction
        elevator.is_door_open = True
        elevator.save()

        # Get the next_request with the smallest timestamp and the same direction as the elevator
        next_request = RequestModel.objects.filter(
            direction=elevator.elev_direction).order_by('timestamp').first()

        if next_request:
            elevator.elev_direction = self.move_elevator(
                elevator, next_request.current_floor)
            elevator.current_floor = next_request.current_floor
            elevator.save()
        else:
            elevator.elev_direction = "Stopped"
            elevator.save()
    else:
        # Check if the elevator is currently at a destination floor
        # by comparing its current_floor with the destination_floor of the latest request
        latest_destination = RequestModel.objects.filter(direction=elevator.elev_direction).aggregate(
            Max('destination_floor'))['destination_floor__max']
        if latest_destination is not None and elevator.current_floor == latest_destination:
            elevator.is_door_open = True
            elevator.save()
        else:
            elevator.is_door_open = False
            elevator.elev_direction = self.move_elevator(
                elevator, elevator.current_floor)
            elevator.save()


def initialize_elevator_system():
    num_elevators = 5
    elevator_system = ElevatorSystem(num_elevators)
    return elevator_system
