from django.db import models

class Room(models.Model):
    RoomName = models.CharField(max_length=100)
    UserName = models.CharField(max_length=100,unique=True)
    private = models.BooleanField(default=False)
    password = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.RoomName

    def is_public(self):
        return not self.private

    def set_password(self, new_password):
        if self.private:
            self.password = new_password
        else:
            raise ValueError("You can only set a password for a private room.")

    def get_room_info(self):
        room_info = f"Room Name: {self.RoomName}\nUser Name: {self.UserName}\n"
        if self.is_public():
            room_info += "This is a public room."
        else:
            room_info += f"This is a private room with the password: {self.password}"
        return room_info
