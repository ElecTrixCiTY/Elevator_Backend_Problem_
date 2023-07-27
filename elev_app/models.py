from django.db import models

class ElevatorModel(models.Model):
    elev_id = models.AutoField(primary_key=True)
    current_floor = models.IntegerField(default=0)
    elev_direction = models.CharField(choices=[('U', "Upward"), ('D', "Downward"), ('S', "Stopped")], max_length=1, default='S')
    door = models.CharField(choices=[('Open', "Open"), ('Close', "Close")], max_length=5, default='Close')
    elev_working = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.current_floor
    


class ElevatorSystemModel(models.Model):
    elev_number = models.IntegerField()

    def __str__(self) -> str:
        return f"Number of elevators in this system = {self.elev_number}"