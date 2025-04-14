document.addEventListener('DOMContentLoaded', function() {
    const fileInput = document.getElementById('file-input');
    const uploadForm = document.getElementById('file-upload-form');

    uploadForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const files = fileInput.files;
        if (files.length === 0) {
            alert('Please select at least one HTML file to upload.');
            return;
        }
        handleFileUpload(files);
    });

    function handleFileUpload(files) {
        const formData = new FormData();
        for (let i = 0; i < files.length; i++) {
            formData.append('htmlFiles', files[i]);
        }

        // Simulate file upload to the server
        setTimeout(() => {
            alert('Files uploaded successfully!');
            updateIndexHTML(files);
        }, 1000);
    }

    function updateIndexHTML(files) {
        const fileList = document.getElementById('html-files');
        for (let i = 0; i < files.length; i++) {
            const file = files[i];
            const listItem = document.createElement('li');
            const link = document.createElement('a');
            link.href = URL.createObjectURL(file);
            link.textContent = file.name;
            listItem.appendChild(link);
            fileList.appendChild(listItem);
        }
    }
});
