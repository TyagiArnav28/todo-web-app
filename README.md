# 📝 To-Do List Web App

A beautiful, modern to-do list web application built with Flask and Python. Keep track of your tasks with a clean and intuitive interface!

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

- ➕ **Add Tasks** - Quickly add new tasks to your list
- ✅ **Mark Complete** - Check off tasks as you complete them
- 🗑️ **Delete Tasks** - Remove tasks you no longer need
- 📊 **Task Statistics** - See your total, active, and completed tasks at a glance
- 🧹 **Clear Completed** - Remove all completed tasks with one click
- 💾 **Persistent Storage** - Your tasks are saved automatically in JSON format
- 📱 **Responsive Design** - Works perfectly on desktop, tablet, and mobile
- 🎨 **Beautiful UI** - Modern gradient design with smooth animations

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
```bash
   git clone https://github.com/TyagiArnav28/todo-web-app.git
   cd todo-web-app
```

2. **Install required packages**
```bash
   pip install -r requirements.txt
```

3. **Run the application**
```bash
   python app.py
```

4. **Open your browser**
   
   Navigate to `http://localhost:5000`

## 📁 Project Structure
```
todo-web-app/
│
├── app.py              # Main Flask application
├── todos.json          # Task storage (created automatically)
├── README.md           # Project documentation
├── requirements.txt    # Python dependencies
│
├── templates/          # HTML templates
│   └── index.html      # Main page template
│
└── static/            # Static files
    └── style.css      # Stylesheet
```

## 💻 How to Use

1. **Add a Task**: Type your task in the input field and click "Add Task" or press Enter
2. **Complete a Task**: Click the circle icon next to a task to mark it as complete
3. **Delete a Task**: Click the trash icon to remove a task
4. **Clear Completed**: Click "Clear Completed" to remove all finished tasks at once

## 🛠️ Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3
- **Data Storage**: JSON
- **Icons**: Font Awesome

## 🎯 Future Enhancements

- [ ] User authentication and multiple user support
- [ ] Task categories/tags
- [ ] Due dates and reminders
- [ ] Priority levels
- [ ] Search and filter functionality
- [ ] Dark mode toggle
- [ ] Export tasks to CSV/PDF

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Arnav Tyagi**
- GitHub: [@TyagiArnav28](https://github.com/TyagiArnav28)

## 🙏 Acknowledgments

- Inspired by various to-do list applications
- Font Awesome for the beautiful icons
- Flask documentation and community

---

⭐ If you found this project helpful, please give it a star!