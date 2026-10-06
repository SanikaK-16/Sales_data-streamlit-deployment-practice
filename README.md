# Streamlit Deployment Practice

A very basic Streamlit + Machine Learning project created for practicing:

- GitHub repository creation
- Git commands
- `requirements.txt`
- Streamlit app deployment

## Project

The app uses a small advertising/sales dataset and trains a simple Linear Regression model.

You enter advertising spend and the app predicts expected sales.

## Files

```text
streamlit_deployment_practice/
├── app.py
├── sales_data.csv
├── requirements.txt
├── .gitignore
└── README.md
```

## Run locally

Open a terminal inside this folder:

```bash
pip install -r requirements.txt
```

Then:

```bash
streamlit run app.py
```

The app should open in your browser.

## Deploy on Streamlit Community Cloud

1. Create a GitHub repository.
2. Upload/push all files from this folder.
3. Go to Streamlit Community Cloud.
4. Sign in with GitHub.
5. Create a new app.
6. Select your GitHub repository.
7. Select the branch (usually `main`).
8. Set the main file to:

```text
app.py
```

9. Click Deploy.

Streamlit will install the packages from `requirements.txt` automatically.

## Git commands

After creating an empty GitHub repository:

```bash
git init
git add .
git commit -m "Initial Streamlit app"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your own repository URL.

## Updating the deployed app

After making changes:

```bash
git add .
git commit -m "Update app"
git push
```

Streamlit Cloud will normally detect the new commit and redeploy the app.
