# 8fit-dev
---
This is a test setup for the 8fit promo page created with Wagtail by Onyeka Aghanenu. This can be run on a server or locally using the dev settings in `8fit/settings`.

To get started on a local server, create a new virtualenv and clone this repo into that folder. Navigate to `8fit-dev` and install the required apps by running:

`pip install -r requirements.txt`

Run the following commands afterwards:

```
python manage.py migrate
python manange.py createsuperuser
python manage.py runserver --settings=8fit.settings.dev
```

You should be good to go.

### Creating a Promo Landing Page

After you log into the admin with the credentials you created in the above commands:
1. Navigate to `Pages > Welcome` where you can create a new child page.
2. Select 'Promo Landing Page' to create a new page.
3. On the New Landing Page there are 3 sections:
  1. The **Hero** title and image and overview
  2. The **Features**, i.e each section of the page highlighting each advertised feature. If you add content to the Overview section, each of these features will have their respective icons placed underneath, linking to their section, as in the example shown.
  3. The **Plan**. Here is where you can add details for the plan including the price, currency, duration and CTA text.
4. To create a new promo plan, navigate to `Snippets > Promo Plans`. For the sake of this demo, you can only add a name and description for now.


**Note**: A Stripe form (non-functional) is added to all promo pages for the sake of this presentation. On a production server, the application is configured to save uploads to AWS using `django-storages` and uses Postgres DB.
