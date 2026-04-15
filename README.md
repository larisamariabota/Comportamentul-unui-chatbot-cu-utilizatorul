# AI Conversation Simulation Model

## Overview

This project is a Python-based simulation of an AI conversation system.  
It models how an AI might respond to user questions using probabilistic behavior and statistical distributions.

The simulation includes:
- Probability of understanding user input
- Response time modeling (exponential distribution)
- User satisfaction modeling (normal distribution)
- Multiple user questions in one session

### Demo 
![](foto/model%20simulare.png)

---


---

## How It Works

The AI does not use real machine learning. Instead, it simulates behavior using probability:

- **Understanding** → Bernoulli trial (random success/failure)
- **Response time** → Exponential distribution
- **Satisfaction** → Normal distribution

---

## Mathematical Models

### Uniform Distribution
Used as a base random generator.

### Exponential Distribution
Models response time:
- fast responses are common
- slow responses are rare

### Normal Distribution
Models user satisfaction:
- most results are near average
- extremes are rare

---

## Requirements

- Python 3.x
- No external libraries required

Built-in modules used:
- `random`
- `math`

---

## How to Run

```bash
python main.py

