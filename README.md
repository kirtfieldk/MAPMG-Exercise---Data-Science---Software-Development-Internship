# Keith Kirtfield Application API

Within this api, a user will be able to add, delete, update, and recieve applications of interns applying for this position.

To use this api:

1. For `GET` all applicants and `POST` applications
   > /api/v1/applicants
2. For `GET` specific applicants, `DELETE` applications, and `PUT` applications
   > /api/v1/applicants/:app_id
3. For `GET` Specific appliations with a name
   > /api/v1/applicants/lastname/:last_name
4. For `GET` Specific appliations by school
   > /api/v1/applicants/school/:school

## Formatting

1. The request body should be simple JSON.
2. For Positions the only open positions is the DEV INTERN.
3. Schools schould be posted in acronyms like VT, VCU, AZ, or UCB.

```
dev intern
```

```json
{
  "first_name": "Keith",
  "last_name": "Kirtfield",
  "position": "Dev Intern",
  "school": "VCU",
  "degree": "Computer Science"
}
```

For the Update request both req below are valid

```json
({
  "first_name": "Ryan",
  "last_name": "Kirtfield",
  "position": "Dev Intern",
  "school": "VCU",
  "degree": "Computer Science"
},
{
  "first_name": "Ryan"
})
```

When updating a position with an invalid position the response will be the original application with no modifications

## Example Response Data

```json
{
  "count": 1,
  "data": [
    {
      "date": "Sun, 10 Nov 2019 17:22:47 GMT",
      "degree": "poly sci",
      "first_name": "jim",
      "id": 82,
      "last_name": "pants",
      "position": {
        "title": "dev intern"
      },
      "school": "au"
    }
  ],
  "success": true
}
```

For delete

```json
{
  "sucess": true,
  "data": []
}
```

## The API contains:

- [x] Local instance of SQL database
- [x] Flask Web Server
- [x] Basic CRUD Functions
- [x] Status Codes and Error Handling
- [x] DockerFile For Universal preformance
- [x] Many Unit Test to Ensure Functionality

## Docker-Compose

I decided to use this specificlly for the volumes tag for automatic code updating without rebuilding.

```
docker-compose up --build
```

## Run

App

```
pthon app.py
```

Test

```
python test.py
```
