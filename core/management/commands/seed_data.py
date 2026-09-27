from django.core.management.base import BaseCommand

from core.models import (
    Certification,
    Education,
    Experience,
    Profile,
    Project,
    Skill,
    SkillCategory,
)


class Command(BaseCommand):
    help = "Populate the database with Shiddanagouda Patil's portfolio content."

    def handle(self, *args, **options):
        Profile.objects.all().delete()
        Profile.objects.create(
            full_name="Shiddanagouda Patil",
            tagline="Software Engineer (Fresher) — Python / Django / DRF / FastAPI",
            summary=(
                "Computer Science & Engineering graduate with strong foundations in Python, "
                "Data Structures & Algorithms, Object-Oriented Programming, SQL, DBMS, and "
                "Operating Systems. Hands-on experience with Django, REST APIs, Git, and "
                "software development, with practical exposure to debugging and problem-solving. "
                "Solved 150+ LeetCode problems covering arrays, linked lists, trees, graphs, "
                "binary search, DFS, BFS, and sliding window techniques. Seeking an entry-level "
                "Software Engineer role to contribute to building reliable and scalable software "
                "solutions."
            ),
            location="Davangere, Karnataka, India",
            email="shiddanagoudapatil839@gmail.com",
            phone="+91 8073273002",
            linkedin_url="https://linkedin.com/in/shiddanagouda",
            github_url="https://github.com/Shiddanagouda-dot",
            leetcode_note="150+ problems solved on LeetCode",
            languages_spoken="English (Professional), Kannada (Native), Hindi (Intermediate)",
        )

        Education.objects.all().delete()
        Education.objects.create(
            institution="GM Institute of Technology, Davangere (VTU)",
            degree="Bachelor of Engineering in Computer Science",
            location="Davangere, Karnataka",
            end_year="2026",
            detail="CGPA: 8.4",
            order=1,
        )

        Experience.objects.all().delete()
        Experience.objects.create(
            role="Python Full Stack Development Trainee",
            organization="QSpiders",
            location="Bangalore, Karnataka",
            start_date="Feb 2026",
            end_date="Present",
            bullet_points=(
                "Completed training in Python, Object-Oriented Programming, Oracle SQL, "
                "HTML, CSS, JavaScript, and Django fundamentals.\n"
                "Practiced REST APIs, HTTP methods, JSON, relational databases, and basic "
                "debugging techniques.\n"
                "Applied Python programming, Pandas, and NumPy through coding exercises and "
                "development practice.\n"
                "Solved 150+ LeetCode problems covering arrays, linked lists, trees, graphs, "
                "binary search, DFS, BFS, sliding window, and other algorithmic techniques."
            ),
            order=1,
        )

        SkillCategory.objects.all().delete()
        skill_map = {
            "Languages": ["Python", "JavaScript", "SQL (Oracle)", "HTML", "CSS"],
            "Backend": ["Django", "Django REST Framework", "FastAPI", "REST APIs", "HTTP Methods", "JSON", "Swagger / OpenAPI"],
            "Databases": ["Oracle SQL", "PostgreSQL", "Relational Database Concepts", "DBMS"],
            "Data & Analysis": ["Pandas", "NumPy"],
            "Data Structures & Algorithms": [
                "Arrays", "Strings", "Linked Lists", "Stacks", "Queues", "Trees", "Graphs",
                "Binary Search", "Two Pointers", "Sliding Window", "DFS", "BFS",
                "Topological Sort", "Disjoint Set (Union-Find)", "Sorting Algorithms",
            ],
            "Core CS & Practice": ["Object-Oriented Programming", "Operating Systems", "Software Testing", "Debugging"],
            "Tools": ["Git", "GitHub", "VS Code", "Uvicorn", "Playwright"],
        }
        for i, (category_name, skills) in enumerate(skill_map.items(), start=1):
            category = SkillCategory.objects.create(name=category_name, order=i)
            for j, skill_name in enumerate(skills, start=1):
                Skill.objects.create(category=category, name=skill_name, order=j)

        Project.objects.all().delete()
        Project.objects.create(
            title="Blockchain-Based Land Registration System",
            year="2025",
            tech_stack="Solidity, PostgreSQL",
            summary="A blockchain-based system for secure land ownership and transfer.",
            bullet_points=(
                "Developed a blockchain-based land registration system for secure land "
                "ownership and transfer.\n"
                "Implemented immutable transaction records to improve transparency and "
                "data integrity."
            ),
            order=1,
        )
        Project.objects.create(
            title="Echo Eats — Voice-Based Food Ordering System",
            year="2025",
            tech_stack="React, Django, MySQL",
            summary="A voice-and-manual food ordering system with AI/LLM intent handling.",
            bullet_points=(
                "Developed a voice-based food ordering system using React, Django, and MySQL.\n"
                "Implemented REST API communication between the frontend and backend and "
                "integrated database operations using MySQL."
            ),
            order=2,
        )
        Project.objects.create(
            title="JavaScript Mini Projects",
            year="2025",
            tech_stack="HTML5, CSS3, JavaScript",
            summary="A set of small JavaScript apps covering DOM manipulation and API integration.",
            bullet_points=(
                "Built a Weather Application using the OpenWeather API to retrieve and "
                "display real-time weather information.\n"
                "Developed an Expense Tracker, Quiz App, To-Do List, Calculator, Digital "
                "Clock, and Stopwatch using JavaScript.\n"
                "Applied DOM manipulation, event handling, and API integration across "
                "multiple applications."
            ),
            order=3,
        )
        Project.objects.create(
            title="FastAPI-Based Landmark API",
            year="2025",
            tech_stack="FastAPI, Uvicorn, Swagger/OpenAPI",
            summary="A documented REST API for looking up landmark data.",
            bullet_points=(
                "Built a FastAPI service with auto-generated Swagger/OpenAPI documentation.\n"
                "Modelled request/response schemas and exposed clean REST endpoints."
            ),
            order=4,
        )
        Project.objects.create(
            title="Object Detection App",
            year="2025",
            tech_stack="OpenCV, TensorFlow, Python",
            summary="An app that detects and labels objects in images in real time.",
            bullet_points=(
                "Used OpenCV and TensorFlow to detect and classify objects from image input.\n"
                "Focused on practical model integration rather than model training from scratch."
            ),
            order=5,
        )
        Project.objects.create(
            title="Appointment Scheduling System",
            year="2025",
            tech_stack="Python, Django",
            summary="A booking system for managing appointment slots and conflicts.",
            bullet_points=(
                "Modelled appointments, availability, and conflict checks.\n"
                "Built CRUD flows for creating, updating, and cancelling bookings."
            ),
            order=6,
        )

        Certification.objects.all().delete()
        Certification.objects.create(name="The Joy of Computing Using Python", provider="NPTEL", year="2024", order=1)
        Certification.objects.create(name="Introduction to Internet of Things", provider="NPTEL", year="2024", order=2)
        Certification.objects.create(name="The Complete Full-Stack Web Development Bootcamp", provider="Udemy", year="2025", order=3)

        self.stdout.write(self.style.SUCCESS("Portfolio data seeded successfully."))
