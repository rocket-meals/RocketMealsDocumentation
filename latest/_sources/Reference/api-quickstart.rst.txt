API Quickstart
==============

For this part of the documentation, we will be using English as the language of choice.

In this quickstart we will be covering the following topics:

- Project Style and Logo
- Canteen Loading
- Food Offer Loading
- Food Image Loading
- Markings Loading


So, in order to use the API, we will quickly go through the steps you need to know to get started. First, let's talk about variables and preambles.

**Preamble**

- For this quickstart, we will be using ``https://rocket-meals.de/rocket-meals/api`` as the base URL for the API. Please replace this with the actual URL of the API.
- By the time of reading, maybe some permissions on the test API have changed. If you encounter any problems, please contact us or test it on the actual API you want to use.
- We are using the generated API routes from our used software [Directus](https://directus.io/). Directus offers a [JavaScript SDK](https://docs.directus.io/guides/sdk/getting-started.html) which could be handy for you.
- In this quickstart, we will be acting as a non-logged-in/guest/public user.

**Step 1: Project Style and Logo**

Request:

.. code-block:: javascript

    https://rocket-meals.de/rocket-meals/api/settings

Response Content:

- This response will contain general information about the project.
- Including the project name, color, and the logo.

Example Response:

.. code-block:: javascript

    {
        "data": {
            "project_name": "Rocket Meals",
            "project_color": "#80BA27",
            "project_logo": "<PROJECT_LOGO_ID>"
        }
    }

The logo can then be accessed via the following URL: ``https://rocket-meals.de/rocket-meals/api/assets/<PROJECT_LOGO_ID>``

**Step 2: Canteen Loading**

Request:

.. code-block:: javascript

    https://rocket-meals.de/rocket-meals/api/items/canteens?fields=*&limit=-1

Response Content:

- This response will contain all canteens that are available in the system.
- The canteens contain a lot of information. We will only cover the most important fields in this quickstart.
- The ``id`` of the canteen is important for the next step.
- The ``alias`` of the canteen is the name of the canteen.
- The ``external_identifier`` is the identifier of the canteen in the related system where the data is coming from (e.g. TL1 or an FTP file).
- Limit is set to ``-1`` to get all canteens.

Example Response:

.. code-block:: javascript

    {
        "data": [
            {
                "id": "<CANTEEN_ID>",
                "alias": "Hauptmensa",
                "external_identifier": "Hauptmensa",
                ...
                "building": "<BUILDING_ID>"
            },
            ...
        ]
    }

We will be using the ``id`` of the canteen for the next step.

**Step 3: Food Offer Loading**

- As we obtained the ``id`` of the canteen, we can now request the food offers for the canteen.
- Our used API offers to pass a query in the URL. If you want to read more about that, you can do so here: [Directus Query](https://docs.directus.io/reference/query.html)
- As ``food offers`` and ``foods`` contain a lot of data, we will only cover the most important fields in this quickstart.
- Please keep in mind that ``food`` and ``foodoffers`` are two different tables in the database. The ``foodoffers`` table contains the actual offers for a specific date and the ``food`` table contains general information about the food.

Variables:

- ``<CANTEEN_ID>``: The ID of the canteen you want to get the food offers for. Please replace this with the actual ID you want to use.
- ``<DATE_BEGIN>``: The date for which you want to get the food offers. Please replace this with the actual date you want to use: e.g. ``2024-05-14T22:00:00.000Z`` in ISO format.
- ``<DATE_END>``: The date for which you want to get the food offers. Please replace this with the actual date you want to use: e.g. ``2024-05-15T21:59:59.999Z`` in ISO format.
- We also filter for ``date`` being ``null`` as some offers are not bound to a specific date e.g. ``daily offers`` like fries or a salad.
- Limit is set to ``-1`` to get all food offers.

Example Request:

.. code-block:: javascript

    https://rocket-meals.de/rocket-meals/api/items/foodoffers?fields=*,food.*,food.translations.*,markings.*&filter={"_and":[{"_or":[{"date":{"_between":["<DATE_BEGIN>","<DATE_END>"]}},{"date":{"_null":true}}]},{"canteen":{"_eq":"<CANTEEN_ID>"}}]}&limit=-1

Response Content:

- This response will contain all ``food offers`` for the ``canteen`` on the specified ``date``.
- The ``food offer`` holds information about: ``prices``, ``nutritional values``, ``food`` and ``markings``.
- The ``food`` holds information about: ``translations``, ``image`` and ``ratings``.

Example Response:

.. code-block:: javascript

    {
        "data": [
            {
                "alias": "Linsen-Mango-Curry Salzkartoffeln",
                "id": "<FOODOFFER_ID>",
                "date": "2024-05-15",
                "price_employee": 6.3,
                "price_guest": 7.9,
                "price_student": 3,
                "calories_kcal": 570,
                "carbohydrate_g": 82.4,
                ...
                "markings": [
                    {
                        "foodoffers_id": "<FOODOFFER_ID>",
                        "id": 752631,
                        "markings_id": "<MARKING_ID>"
                    },
                    ...
                ],
                "food": {
                    "alias": "Linsen-Mango-Curry Salzkartoffeln",
                    "id": "<FOOD_ID>",
                    "image": "<IMAGE_ASSET_ID>",
                    "image_remote_url": null,
                    "rating_amount": null,
                    "rating_average": null,
                    ...
                    "translations": [
                        {
                            "be_source_for_translations": false,
                            "foods_id": "<FOOD_ID>",
                            "id": 1952,
                            "languages_code": "de-DE",
                            "let_be_translated": true,
                            "name": "Pellkartoffeln"
                        },
                        ...
                    ]
                }
            },
            ...
        ]
    }

**Step 4: Food Image Loading**

- As we have the ``image`` of the ``food`` from the ``food offer``, we can now request the image.
- The ``image`` id in our example is ``<IMAGE_ASSET_ID>``.

Example Request:

.. code-block:: javascript

    https://rocket-meals.de/rocket-meals/api/assets/<IMAGE_ASSET_ID>

Response Content:

- This response will contain the image of the ``food``.

Future Information:

- You can also request thumbnails of the image or use preset transformations like ``width`` and ``height`` in the URL.
- More can be found here: [Request a Thumbnail](https://docs.directus.io/reference/files.html#requesting-a-thumbnail)


**Step 5: Markings Loading**

- For each ``food offer`` we can read in the ``markings`` which ``<MARKING_ID>`` are assigned.
- We now want to get all ``markings`` in the system.

Example Request:

.. code-block:: javascript

    https://rocket-meals.de/rocket-meals/api/items/markings?fields=*,translations.*&limit=-1

Response Content:

- This response will contain all ``markings`` in the system.
- The ``markings`` contain information about: ``translations``.
- The ``markings`` will have an ``external_identifier`` which is the identifier of the marking in the related system where the data is coming from (e.g. TL1 or an FTP file).
- We highly reccoment to use the ``external_identifier`` for the identification of the marking and using the ``translations`` name (if available) or the ``alias`` for the display of the marking.
- The ``markings`` also may contain information about an ``image``, ``image_remote_url`` or ``icon``.

Example Response:

.. code-block:: javascript

    {
        "data": [
            {
                "id": "<MARKING_ID>",
                "alias": "Roggen Gluten",
                "external_identifier": "20A",
                ...
                "translations": [
                    {
                        "languages_code": "de-DE",
                        "name": "enthält Glutenhaltiges Getreide: Roggen",
                        ...
                    },
                    ...
                ]
            },
            ...
        ]
    }



