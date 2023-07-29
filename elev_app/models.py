from django.db import models

class ElevatorModel(models.Model):
    elev_id = models.AutoField(primary_key=True)
    current_floor = models.IntegerField(default=0)
    elev_direction = models.CharField(choices=(('Up', "Up"), ('Down', "Down"), ('Stopped', "Stopped")), max_length=7, default='Stopped')

    door = models.CharField(choices=[('Open', "Open"), ('Close', "Close")], max_length=5, default='Close')
    elev_working = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'Elevator {self.elev_id} in floor:{self.current_floor}'

    


class RequestModel(models.Model):
    current_floor = models.IntegerField()


    floor_direction = models.CharField(choices=(
    ('Up', "Up"), ('Down', "Down"), ('Stopped', "Stopped")), max_length=7, default='Stopped')

    destination_floor = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

   