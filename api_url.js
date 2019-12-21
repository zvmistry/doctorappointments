// Copyright 2019, Zeus Mistry
// Returns proper urls
define([], function () {
    var root = '/api';
    var apiUrl = {
        doctors: function() {
            return root+'/doctors';
        },
        doctorAppointments: function(doctorId) {
            return root+'/doctors/'+doctorId;
        }
    };
    return apiUrl;
});
