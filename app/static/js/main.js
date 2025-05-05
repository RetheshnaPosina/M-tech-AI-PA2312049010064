document.addEventListener('DOMContentLoaded', function() {
    const startBtn = document.getElementById('startBtn');
    const stopBtn = document.getElementById('stopBtn');
    const uploadBtn = document.getElementById('uploadBtn');
    const videoUpload = document.getElementById('videoUpload');
    const totalCount = document.getElementById('totalCount');
    const currentCount = document.getElementById('currentCount');

    // Update stats periodically
    function updateStats() {
        fetch('/get_stats')
            .then(response => response.json())
            .then(data => {
                totalCount.textContent = data.total_count;
                currentCount.textContent = data.current_objects || 0;
                setTimeout(updateStats, 1000);
            });
    }

    // Button event listeners
    startBtn.addEventListener('click', () => {
        fetch('/start_camera')
            .then(response => response.json())
            .then(data => console.log(data.message));
    });

    stopBtn.addEventListener('click', () => {
        fetch('/stop_camera')
            .then(response => response.json())
            .then(data => console.log(data.message));
    });

    uploadBtn.addEventListener('click', () => {
        const file = videoUpload.files[0];
        if (!file) {
            alert('Please select a video file first');
            return;
        }

        const formData = new FormData();
        formData.append('file', file);

        fetch('/upload', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message || 'Video uploaded successfully');
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });

    // Start updating stats
    updateStats();
});