# Copyright 2019, Zeus Mistry
import json
from flask import request  # python flask app

from doctor_service import DoctorService

doctor_service = DoctorService() # also initialized doctors and resets everything

# All function assume authentication is done ... imagine an authentication decorator

@api.route('/doctors', methods=['GET'])
def get_all_doctors():
    doctors = doctor_service.get_all_doctors()
    return json.dumps({'success': True, 'doctors': doctors})


@api.route('/doctors/<doctor_id>/appointments', methods=['GET'])
def get_doctor_appointments(doctor_id):
    appointment_date = request.json.get('appointment_date')  # Assumes format 'YYYY-MM-DD'
    try:
        appointments = doctor_service.get_doctor_appointments_for_date(doctor_id, appointment_date)
        return json.dumps({'success': True, 'appointments': appointments})
    except Exception as e:
        return json.dumps({'success': False, 'error': e.message})


@api.route('/doctors/<doctor_id>/appointments', methods=['DELETE'])
def delete_doctor_appointment(doctor_id):
    appointment_id = request.json.get('appointment_id')
    try:
        doctor_service.delete_doctor_appointment(doctor_id, appointment_id)
        return json.dumps({'success': True})
    except Exception as e:
        return json.dumps({'success': False, 'error': e.message})


@api.route('/doctors/<doctor_id>/appointments', methods=['POST'])
def add_doctor_appointment(doctor_id):
    patient_first_name = request.json.get('patient_first_name')
    patient_last_name = request.json.get('patient_last_name')
    appointment_date = request.json.get('appointment_date')
    appointment_timepp = request.json.get('appointment_time')
    appointment_kind = request.json.get('appointment_kind')
    try:
        appointment_id = doctor_service.add_doctor_appointment(
            doctor_id, patient_first_name, patient_last_name, appointment_date, appointment_time, appointment_kind)
        return json.dumps({'success': True, 'appointment_id': appointment_id})
    except Exception as e:
        return json.dumps({'success': False, 'error': e.message})
