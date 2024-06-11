document.addEventListener('DOMContentLoaded', function() {
    var fileInputBtn = document.querySelector('.btn-light');
    var fileInput = document.getElementById('id_files');

    fileInputBtn.addEventListener('click', function() {
        fileInput.click();
    });

    var messages = document.querySelectorAll('.alert');
    messages.forEach(function(message, index) {
        setTimeout(function() {
            message.style.display = 'none';
        }, 5000); // Hide messages after 5 seconds
    });

    if ($('input[type="file"]')[0]) {
        var label = document.querySelector('label[for="et_pb_contact_brand_file_request_0"]');
        label.ondragover = function() {
            this.className = "et_pb_contact_form_label changed";
            return false;
        };
        label.ondragleave = function() {
            this.className = "et_pb_contact_form_label";
            return false;
        };
        label.ondrop = function(e) {
            e.preventDefault();
            var fileNames = e.dataTransfer.files;
            for (var x = 0; x < fileNames.length; x++) {
                console.log(fileNames[x].name);
                $=jQuery.noConflict();
                $('label[for="et_pb_contact_brand_file_request_0"]').append("<div class='file_names'>"+ fileNames[x].name +"</div>");
            }
        };
        $('#et_pb_contact_brand_file_request_0').change(function() {
            var fileNames = $('#et_pb_contact_brand_file_request_0')[0].files[0].name;
            $('label[for="et_pb_contact_brand_file_request_0"]').append("<div class='file_names'>"+ fileNames +"</div>");
            $('label[for="et_pb_contact_brand_file_request_0"]').css('background-color', '##eee9ff');
        });
    }
});
