# Spredo Test Task Submission

## Overview

This project is a simple full-stack application that fetches cryptocurrency data from CoinGecko, filters it in the backend, and displays it in the frontend.

## Stack

- Backend: Python + Flask
- Frontend: React + Vite

## Features Completed

### Backend
- CoinGecko API fetch
- Filtering logic
- /projects endpoint

### Frontend
- Project table
- Search by name
- FDV max filter
- Sorting by Market Cap
- Sorting by 24h Volume

## How to Run

### Backend

pip install -r requirements.txt  
python backend/app.py

### Frontend

cd frontend  
npm install  
npm run dev

## Limitations

- Uses mock fallback data if CoinGecko unavailable
- Basic styling only

## AI Workflow

Used Cursor for scaffolding, Claude for backend filtering logic, ChatGPT for debugging frontend state issues. Final code reviewed manually.
