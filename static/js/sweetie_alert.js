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

function confirmDelete(recordId) {
    Swal.fire({
        title: 'Are you sure?',
        text: "You won't be able to revert this!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#3085d6',
        confirmButtonText: 'Yes, delete it!'
    }).then((result) => {
        if (result.isConfirmed) {
            document.getElementById('delete-form-' + recordId).submit()
        }
    })
}

// for records_view sweetie alert
// This script should be included after the SweetAlert2 library is loaded
document.addEventListener('DOMContentLoaded', function () {
    // Delete button handler
    document.querySelectorAll('.delete-btn').forEach((button) => {
        button.addEventListener('click', function (e) {
            e.preventDefault() // This is CRUCIAL to prevent any default behavior
            e.stopPropagation() // Prevent event bubbling

            const form = this.closest('form')

            Swal.fire({
                title: 'Are you sure?',
                text: "You won't be able to revert this!",
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#d33',
                cancelButtonColor: '#3085d6',
                confirmButtonText: 'Yes, delete it!'
            }).then((result) => {
                if (result.isConfirmed) {
                    form.submit() // Only submit if confirmed
                }
            })
        })
    })
})
// Example usage to avoid unused function warnings
// showAlert();
// showError();
