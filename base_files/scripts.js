/* 
  This is a SAMPLE FILE to get you started.
  Please, follow the project instructions to complete the tasks.
*/

document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form'); // Asegúrate de que tu formulario tenga este ID

    if (loginForm) {
        loginForm.addEventListener('submit', async (event) => {;
});

function handleLoginSubmit(event) {
    event.preventDefault();
    const email = document.getElementById('email').value; // Asume que tu formulario tiene un campo con ID 'email'
    const password = document.getElementById('password').value; // Asume que tu formulario tiene un campo con ID 'password'

    fetch('URL_DEL_ENDPOINT_DE_LOGIN', { // Reemplaza con la URL real de tu API
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            email: email,
            password: password,
        }),
    })
    .then(response => response.json())
    .then(data => { // Aquí irá el código para manejar la respuesta de la API
        if (data.token) { // Asume que la API responde con un objeto que contiene un 'token' en caso de éxito
            document.cookie = `token=${data.token}; path=/`; // Almacena el token en una cookie
            window.location.href = 'index.html'; // Redirige al usuario a la página principal
        } else {
            alert('Login failed: ' + data.message); // Muestra un mensaje de error
        }
    })

    .catch((error) => {
        console.error('Error:', error);
        // Aquí puedes manejar errores de la solicitud
    });
}