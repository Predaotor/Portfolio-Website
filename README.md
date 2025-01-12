# Portfolio Website for a Python Backend Developer

## Overview
This project is a portfolio website designed to showcase the skills, projects, and experience of a Python backend developer. The website features a clean and professional design, providing an interactive user experience.

## Features
- Home page with a hero section and call-to-action buttons.
- About Me part detailing background, skills, and personal attributes.
- Projects page displaying various projects with descriptions and tech stacks.


## Project Structure
```
portfolio-website
├── app
│   ├── app.py
       config.py
│   ├── templates
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── projects.html
│   ├── static
│   │   ├── css
│   │   │   └── styles.css
│   │   ├── js
│   │   │   └── scripts.js
│   │   └── images
│   └── views.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/portfolio-website.git
   ```
2. Navigate to the project directory:
   ```
   cd portfolio-website
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Run the application:
   ```
   python src/app.py
   ```
2. Open your web browser and go to `http://127.0.0.1:5000` to view the website.

## Future Enhancements
- Implement a light/dark mode toggle.
- Add user authentication for blog comments.
- Integrate analytics to track visitor interactions.

## License
This project is licensed under the MIT License.