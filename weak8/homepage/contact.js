document.addEventListener('DOMContentLoaded', function() {
    const contactForm = document.getElementById('contactForm');
    const sendButton = document.getElementById('sendButton');
    const formStatus = document.getElementById('formStatus');
    
    if (sendButton) {
        sendButton.addEventListener('click', function() {
            // Get form values
            const name = document.getElementById('name').value.trim();
            const email = document.getElementById('email').value.trim();
            const message = document.getElementById('message').value.trim();
            
            // Simple validation
            if (!name || !email || !message) {
                showStatus('Please fill in all fields', 'error');
                return;
            }
            
            if (!isValidEmail(email)) {
                showStatus('Please enter a valid email address', 'error');
                return;
            }
            
            // Create email content
            const subject = `Contact from ${name} via Portfolio Site`;
            const body = `Name: ${name}\nEmail: ${email}\n\nMessage:\n${message}`;
            
            // Create mailto URL
            const mailtoUrl = `mailto:mdalmahmud023@gmail.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
            
            // Open default mail client
            window.location.href = mailtoUrl;
            
            // Show success message
            showStatus('Opening your email application...', 'success');
            
            // Clear form
            contactForm.reset();
        });
    }
    
    // Function to validate email format
    function isValidEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }
    
    // Function to show status messages
    function showStatus(message, type) {
        formStatus.textContent = message;
        formStatus.className = 'mt-3';
        
        if (type) {
            formStatus.classList.add(type);
        }
        
        // Clear status after 5 seconds if it's a success message
        if (type === 'success') {
            setTimeout(() => {
                formStatus.textContent = '';
                formStatus.className = 'mt-3';
            }, 5000);
        }
    }
});
