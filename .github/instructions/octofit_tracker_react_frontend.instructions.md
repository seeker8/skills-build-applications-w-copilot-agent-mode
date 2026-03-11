---
applyTo: "octofit-tracker/frontend/**"
---
# Octofit-tracker Fitness App React frontend Guidelines

## REACT Frontend App structure

Make sure in all commands we point to the `octofit-tracker/frontend` directory

```bash
npx create-react-app octofit-tracker/frontend --template cra-template --use-npm

npm install bootstrap --prefix octofit-tracker/frontend

# Add the Bootstrap CSS import at the very top of src/index.js:
sed -i "1iimport 'bootstrap/dist/css/bootstrap.min.css';" octofit-tracker/frontend/src/index.js

npm install react-router-dom --prefix octofit-tracker/frontend

```

## Images for the OctoFit Tracker App

The image to use for the app is in the root of this repository docs/octofitapp-small.png
Let's style this like App.css and make it look nice.

- Let's make the App.js and all components javascript files in the app are consistent with the following:
  - Use bootstrap tables for the data in all javascript components.
  - Use bootstrap buttons for the buttons.
  - Use bootstrap headings for the headings.
  - Use bootstrap links for the links.
  - Use bootstrap navigation for the navigation menu.
  - Use bootstrap forms for the forms.
  - Use bootstrap cards for the cards.
  - Use bootstrap modals for the modals.
  - Consistent table layouts for all components data.