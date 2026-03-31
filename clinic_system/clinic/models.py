from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    max_patients = models.IntegerField()

    def __str__(self):
        return f"{self.doctor.name} - {self.date}"

class Appointment(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE)
    schedule = models.ForeignKey('Schedule', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='Booked')

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super(Appointment, self).save(*args, **kwargs)

        if is_new:
            from .models import Token  # ✅ force import

            count = Token.objects.filter(
                appointment__schedule=self.schedule
            ).count()

            Token.objects.create(
                appointment=self,
                token_number=count + 1,
                status='Waiting'
            )
            
            print(f"📩 Notification: Appointment confirmed for {self.patient.name}")
            print(f"🪪 Token Number: {count + 1}")

    def __str__(self):
        return f"{self.patient.name} - {self.doctor.name}"

class Token(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    token_number = models.IntegerField()
    status = models.CharField(max_length=20, default='Waiting')

    def __str__(self):
        return f"Token {self.token_number}"

# Create your models here.
