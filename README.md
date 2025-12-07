# 🌌 PhysicaSim  
**Interactive Physics + Algorithms Simulator**  
*A fusion of physics, data structures & algorithms, and real-time visualization.*

PhysicaSim is a full-stack learning and visualization platform that simulates real-world physics systems while demonstrating the algorithms that power them. This project is designed to strengthen fundamental DSA concepts through intuitive and visually rich physics simulations.

---

## 🚀 MVP Modules (v1.0)

### 1️⃣ Projectile Motion Simulator  
- Real-time projectile visualization  
- Adjustable angle, initial velocity, gravity  
- Trajectory graph (height vs time)  
- Numerical time-step integration  
- Ground impact detection using binary search  

### 2️⃣ N-Body Gravity Simulator (Brute Force)  
- Newtonian gravitational interactions  
- O(n²) force calculation  
- Time-step velocity & position updates  
- Orbital patterns & energy behavior  
- Adjustable particle count and parameters  

### 3️⃣ Barnes–Hut Quadtree Optimized N-Body  
- Spatial partitioning using Quadtrees  
- O(n log n) approximation of gravitational forces  
- Major performance boost vs brute force  
- Visual quadtree debugging mode (optional)  
- Side-by-side FPS comparison panel  

---

# 🧠 Why PhysicaSim?  
PhysicaSim blends **physics**, **algorithms**, and **visual learning**, making DSA more intuitive and enjoyable.

### Key Skills You Will Learn
- Numerical simulations  
- Algorithm design & optimization  
- Data structures: arrays, trees, quadtrees  
- Complexity analysis (O(n²) → O(n log n))  
- Real-time rendering using Canvas/SVG  
- Frontend architecture with Angular  
- Backend API development with FastAPI  
- Performance engineering & profiling  

---

# 🏗️ Tech Stack

**Frontend:** Angular 17, TypeScript, Canvas/SVG  
**Backend:** FastAPI, Python 3.10+, Uvicorn  
**DevOps:** Docker, GitHub Actions  
**Deployment:** Vercel/Netlify (frontend), Render/Heroku (backend)

---

# 📁 Project Structure

physicasim/  
├── frontend/  
│   └── ui/                 # Angular application  
├── backend/  
│   ├── app/                # Backend logic  
│   ├── main.py             # FastAPI entrypoint  
│   ├── run.sh              # Backend launcher  
│   └── requirements.txt    # Python dependencies  
├── Dockerfile              # Container config  
├── docker-compose.yml      # Local development stack  
└── README.md  

---

# ⚙️ Running the Project

## ▶️ Start Backend (FastAPI)
cd backend  
./run.sh  

Backend runs at:  
http://localhost:8000  

---

## ▶️ Start Frontend (Angular)
cd frontend/ui  
ng serve  

Frontend runs at:  
http://localhost:4200  

---

# 🧩 Key Algorithms Implemented

### ➤ Projectile Motion  
- Discrete time-step simulation  
- Numerical integration  
- Height/time tracking  
- Binary search for collision time  

### ➤ N-Body Simulation (Brute Force)  
- Pairwise gravitational force computation  
- O(n²) complexity analysis  
- Vector arithmetic  
- Stable integration loop  

### ➤ Barnes–Hut Algorithm  
- Quadtree construction  
- Center of mass aggregation  
- θ-threshold approximation  
- O(n log n) performance  
- Significant speedup vs brute-force  

---

# 📈 Performance Dashboard
PhysicaSim includes tools to compare:  
- Brute force FPS vs Optimized FPS  
- Quadtree size and depth  
- Approximation error  
- Particle count scaling  
- Execution time per frame  

These charts make the project extremely strong for resume + interviews.

---

# 📦 Roadmap (Future Releases)

### v1.1 — Expanded Physics  
- Wave simulations  
- Cloth simulation (mass-spring system)  
- Fluid-like particles  
- Energy graphs  

### v2.0 — Advanced Algorithms  
- Verlet integration  
- Runge–Kutta solvers  
- Spatial hashing  
- Sweep & prune collision detection  

### v3.0 — User Experience  
- Save/load presets  
- Public preset gallery  
- Interactive math/physics tutorials  
- “Explain this algorithm” automated walkthrough  

---

# 👤 Author
**Shivansh Singh**  
Full-Stack Developer (Angular + Python)  
LinkedIn: https://www.linkedin.com/in/shivanshsingh3345  

---

# 🎥 Demo
Coming soon — add a short GIF or video demo after completing the first module.

---

# 📜 License
MIT License
