let form = document.querySelector('#personForm');

form.addEventListener('submit', async (event) => {
    event.preventDefault(); // Prevent default form submission behavior

    try {
        let formData = new FormData(form);
        let name = formData.get('name');
        let age = formData.get('age');

        const response = await fetch('http://127.0.0.1:8000/api1/per', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ name, age })
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        console.log('Data added successfully:', await response.json());
    } 
    
    catch (error) {
        console.error('Error posting data:', error);
    }
});

