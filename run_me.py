# Copyright 2019, Zeus Mistry
import json

from doctor_service import DoctorService

doctor_service = DoctorService() # also initialized doctors and resets everything

# Purpose of this script is to test how the backend would work form the api-level down

def get_all_doctors():
    doctors = doctor_service.get_all_doctors()
    print json.dumps({'success': True, 'doctors': doctors})


def get_doctor_appointments(doctor_id, appointment_date):
    try:
        appointments = doctor_service.get_doctor_appointments_for_date(doctor_id, appointment_date)
        print json.dumps({'success': True, 'appointments': appointments})
    except Exception as e:
        print json.dumps({'success': False, 'error': e.message})


def delete_doctor_appointment(doctor_id, appointment_id):
    try:
        doctor_service.delete_doctor_appointment(doctor_id, appointment_id)
        print json.dumps({'success': True})
    except Exception as e:
        print json.dumps({'success': False, 'error': e.message})


def add_doctor_appointment(doctor_id, patient_first_name, patient_last_name, date, time, kind):
    try:
        appointment_id = doctor_service.add_doctor_appointment(doctor_id, patient_first_name, patient_last_name, date, time, kind)
        print json.dumps({'success': True, 'appointment_id': appointment_id})
    except Exception as e:
        print json.dumps({'success': False, 'error': e.message})


if __name__ == '__main__':
    run_service = 'Y'
    print "Hello and welcome to Doctor Appointments"
    print "For a list of doctors type: 'doctors'"
    print "For a list of doctors appointments: 'appointments, doctor_id, date' - date format: 'YYYY-MM-DD"
    print "To delete a doctors appointments: 'delete, doctor_id, appointment_id'"
    print "To add an appointments: 'add, doctor_id, patient_first_name, patient_last_name, date, time, kind' - date format: 'YYYY-MM-DD', time format: 'HH:MM', kind == 'New Patient', 'Follow-up'"
    while run_service == 'Y':
        print("")
        command = input("Please input command: ")
        params = command.split(',')
        if params[0] == 'doctors':
            get_all_doctors()
        elif params[0] == 'appointments':
            get_doctor_appointments(params[1].strip(), params[2].strip())
        elif params[0] == 'delete':
            delete_doctor_appointment(params[1].strip(), params[2].strip())
        elif params[0] == 'add':
            add_doctor_appointment(params[1].strip(), params[2].strip(), params[3].strip(), params[4].strip(), params[5].strip(), params[6].strip())
        else:
            print "Invalid command given"
        run_service = input("Would you like to continue? 'Y' for yes, 'N' for no: ")

    print("Thank you, See you Next Time")
    exit()
