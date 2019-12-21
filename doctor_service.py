    # Copyright 2019, Zeus Mistry
import time
import uuid


class DoctorService(object):

    def __init__(self):
        # {doctor_id: {doctor_id, first_name, last_name}}
        d_id1 = str(uuid.uuid4())
        d_id2 = str(uuid.uuid4())
        d_id3 = str(uuid.uuid4())
        self._DOCTORS = {
            d_id1: {'id': d_id1, 'first_name': 'Julius', 'last_name': 'Hibbert'},
            d_id2: {'id': d_id2, 'first_name': 'Algemop', 'last_name': 'Krieger'},
            d_id3: {'id': d_id3, 'first_name': 'Nick', 'last_name': 'Riviera'} 
        }

        # {appointment_id: {appointment_id, patient_first_name, patient_last_name, date, time, kind}}
        self._APPOINTMENTS = {}

        # {doctor_id: [appointment_id]}
        self._DOCTOR_APPOINTMENTS = {}


    def _validate_appointment_time(self, appointment_time):
        try:
            time.strptime(appointment_time, '%H:%M')
        except ValueError:
            raise Exception('Invalid appointment time format given')


        hour = int(appointment_time.split(':')[0])
        if hour < 8 or hour > 16:
            raise Exception('Invalid time for appointment given. Appointment can only be scheduled between hours are between 8 AM and 5 PM only.')

        mins = int(appointment_time.split(':')[1])
        if mins % 15 != 0:
            raise Exception('Invalid start time for appointment given. Start time must be 0 mins, 15 mins, 30 mins, or 45 mins past the hour')

    def _validate_doctor(self, doctor_id):
        if doctor_id not in self._DOCTORS:
            raise Exception('Invalid doctor given')

    def get_all_doctors(self):
        return self._DOCTORS

    def get_doctor_appointments_for_date(self, doctor_id, appointment_date):
        self._validate_doctor(doctor_id)
        appointments = []
        return [self._APPOINTMENTS[a_id] for a_id in self._DOCTOR_APPOINTMENTS.get(doctor_id, []) if appointment_date == self._APPOINTMENTS[a_id]['date']]


    def delete_doctor_appointment(self, doctor_id, appointment_id):
        self._validate_doctor(doctor_id)
        if appointment_id not in self._APPOINTMENTS:
            raise Exception('Invalid appointment given')

        del _APPOINTMENTS[appointment_id]
        del _DOCTOR_APPOINTMENTS[doctor_id]

    def add_doctor_appointment(self, doctor_id, patient_first_name, patient_last_name, appointment_date, appointment_time, appointment_kind):
        self._validate_doctor(doctor_id)

        if appointment_kind not in ['New Patient', 'Follow-up']:
            raise Exeption('Invalid appointment kind given')

        if not patient_first_name or not patient_last_name:
            raise Exception('Invalid patient name')

        self._validate_appointment_time(appointment_time)


         # TODO: validate time --- a time check to see if time is within business hours

        # ensure that patient doesn't already have an appointment on the same day
        appointments = self.get_doctor_appointments_for_date(doctor_id, appointment_date)

        for appointment in appointments:
            if appointment['patient_first_name'] == patient_first_name and appointment['patient_last_name'] == patient_last_name:
                raise Exception('Patient already has appointment for the given date')
            if appointment['time'] == appointment_time:
                raise Exception('Doctor already has another appointment at the same time')

        # add the appointment
        appointment_id = str(uuid.uuid4())
        self._APPOINTMENTS[appointment_id] = {
            'id': appointment_id,
            'patient_first_name': patient_first_name,
            'patient_last_name': patient_last_name,
            'date': appointment_date,
            'time': appointment_time,
            'kind': appointment_kind
        }
        return appointment_id











