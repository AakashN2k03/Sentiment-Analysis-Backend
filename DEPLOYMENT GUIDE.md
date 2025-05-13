# 🎯 Sentiment Analysis Web App

A full-stack web application for sentiment analysis using a React frontend and FastAPI backend.

## 📝 Overview

This project provides a user-friendly interface for performing sentiment analysis on text. Users can enter text through the React frontend, which sends the data to a FastAPI backend that uses a machine learning model to predict the sentiment.

## ⚙️ Tech Stack

- 🧠 **Backend**: FastAPI + Scikit-learn
- 💻 **Frontend**: React.js
- ☁️ **Deployment**: Render (backend) & Vercel (frontend)

## 🏗️ Project Structure

```
sentiment-analysis-app/
├── frontend/          # React frontend application
└── backend/           # FastAPI backend application
    ├── main.py        # FastAPI application entry point
    ├── requirements.txt
    ├── model.pkl      # Trained sentiment analysis model
    └── vectorizer.pkl # Feature vectorizer
```

## ✅ Prerequisites

Before deployment, ensure you have:

- Complete React app in the `frontend/` folder
- Complete FastAPI app in the `backend/` folder with:
  - `main.py` (FastAPI application)
  - `requirements.txt` (Python dependencies)
  - `model.pkl` (Trained sentiment model)
  - `vectorizer.pkl` (Text vectorizer)
- A GitHub account

## 🚀 Deployment Guide

### 1. Deploy Backend on Render

1. Push your `backend/` folder to a GitHub repository
2. Go to [Render](https://render.com) and sign in
3. Click on "New Web Service"
4. Connect your GitHub backend repository
5. Configure the service:
   - **Name**: Choose a name for your service (e.g., `sentiment-analysis-api`)
   - **Environment**: Python 3.11
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port 10000`
   - **Plan**: Free (or choose paid plan for better performance)
6. Click "Create Web Service"
7. Wait for deployment to complete
8. Copy your live backend URL: `https://your-backend.onrender.com`

### 2. Update Frontend API URL

Update your React app (`frontend/src/App.js`) to use the new backend URL:

**Option 1**: Directly update the Axios call:
```js
axios.post("https://your-backend.onrender.com/predict/", {
  text: input,
});
```

**Option 2**: Use an environment variable (recommended):

Create a `.env` file in your frontend directory:
```
REACT_APP_API_URL=https://your-backend.onrender.com
```

Then update your Axios call:
```js
axios.post(`${process.env.REACT_APP_API_URL}/predict/`, { 
  text: input 
});
```

### 3. Deploy Frontend on Vercel

1. Push your `frontend/` folder to a GitHub repository
2. Go to [Vercel](https://vercel.com) and sign in
3. Click "New Project"
4. Import your GitHub frontend repository
5. Configure the project:
   - Set root directory to `frontend` if needed
   - Add environment variables (if using `.env`):
     - Key: `REACT_APP_API_URL`
     - Value: `https://your-backend.onrender.com`
6. Click "Deploy"
7. Once deployment is complete, you'll get a live frontend URL: `https://your-app.vercel.app`

## ✅ Recommended Deployment Order

1. **Deploy Backend First** - Get the live backend URL
2. **Update Frontend** with backend URL
3. **Deploy Frontend**

## 🔧 Troubleshooting

- **CORS Issues**: Ensure your backend allows requests from your frontend domain
- **Environment Variables**: Double-check your environment variable configuration
- **API Endpoints**: Verify that API endpoint paths match between frontend and backend

## 🚩 Next Steps

- Add user authentication
- Implement result saving functionality
- Add more advanced NLP features
- Improve UI/UX with visualization of sentiment scores

## 📄 License

MIT
