# Celebrate-Mate





<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CelebrateMate - Reminders</title>
    <style>
        body {
            font-family: Times New Roman, cursive;
            margin: 0;
            padding: 0;
            background-color: #f4f4f9;
            color: #333;
        }

        header {
            background-color: #4CAF50;
            color: white;
            text-align: center;
            padding: 1em 0;
        }

        main {
            max-width: 800px;
            margin: 2em auto;
            padding: 1em;
            background-color: #fff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        h1, h2 {
            color: #333;
        }

        form {
            display: flex;
            flex-direction: column;
        }

        label {
            margin-top: 1em;
        }

        input, select {
            padding: 0.5em;
            margin-bottom: 1em;
            border: 1px solid #ddd;
            border-radius: 4px;
        }

        button {
            padding: 0.5em;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }

        button:hover {
            background-color: #45a049;
        }

        #remindersList {
            margin-top: 2em;
        }

        #reminderList {
            list-style-type: none;
            padding: 0;
        }

        #reminderList li {
            background-color: #f9f9f9;
            border: 1px solid #ddd;
            padding: 1em;
            margin-bottom: 0.5em;
            border-radius: 4px;
        }

        footer {
            text-align: center;
            padding: 1em 0;
            background-color: #4CAF50;
            color: white;
            position: fixed;
            bottom: 0;
            width: 100%;
        }
    </style>
</head>
<body>
    <header>
        <h1>Welcome to CelebrateMate</h1>
        <p>Automated Birthday and Anniversary Reminders</p>
    </header>
    <main>
        <section id="reminders">
            <h2>Set Your Reminders</h2>
            <form id="reminderForm">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
                
                <label for="date">Date:</label>
                <input type="date" id="date" name="date" required>
                
                <label for="type">Type:</label>
                <select id="type" name="type">
                    <option value="birthday">Birthday</option>
                    <option value="anniversary">Anniversary</option>
                </select>
                
                <label for="contact">Contact Method:</label>
                <select id="contact" name="contact">
                    <option value="sms">SMS</option>
                    <option value="email">Email</option>
                </select>
                
                <button type="submit">Add Reminder</button>
            </form>
        </section>
        <section id="remindersList">
            <h2>Your Reminders</h2>
            <ul id="reminderList"></ul>
        </section>
    </main>
    <footer>
        <p>&copy; 2024 CelebrateMate. All rights reserved.</p>
    </footer>
    <script>
        document.getElementById('reminderForm').addEventListener('submit', function(event) {
            event.preventDefault();
            
            const name = document.getElementById('name').value;
            const date = document.getElementById('date').value;
            const type = document.getElementById('type').value;
            const contact = document.getElementById('contact').value;
            
            fetch('/api/reminders', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ name, date, type, contact })
            })
            .then(response => response.json())
            .then(data => {
                if (data.message) {
                    alert(data.message);
                    fetchReminders();  // Update the list of reminders
                } else if (data.error) {
                    alert(data.error);
                }
            })
            .catch(error => console.error('Error:', error));
        });

        function fetchReminders() {
            fetch('/api/reminders')
                .then(response => response.json())
                .then(data => {
                    const reminderList = document.getElementById('reminderList');
                    reminderList.innerHTML = '';
                    data.forEach(reminder => {
                        const listItem = document.createElement('li');
                        listItem.innerHTML = `<strong>${reminder.name}</strong> - ${reminder.type} on ${reminder.date} (${reminder.contact})`;
                        reminderList.appendChild(listItem);
                    });
                })
                .catch(error => console.error('Error:', error));
        }

        // Load reminders when the page loads
        window.onload = fetchReminders;
    </script>
</body>
</html>

