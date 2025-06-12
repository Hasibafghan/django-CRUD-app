// Make sure SweetAlert2 is loaded before using Swal
// <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>

function showAlert() {
    Swal.fire({
        title: 'Auto close alert!',
        text: 'This will close in 3 seconds.',
        // timer: 2000, // time in milliseconds (3000 ms = 3 seconds)
        timerProgressBar: true, // optional: show a nice progress bar
    });
}

function showError() {
    Swal.fire({
        icon: 'error',
        title: 'Error!',
        text: 'Something went wrong. Please try again later.',
        confirmButtonText: 'OK'
    });
}

// Example usage to avoid unused function warnings
// showAlert();
// showError();
