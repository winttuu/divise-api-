# divise-api-

This api was developed to convert the Argentina courrency to USD

This project uses the View class provided by Django, from which we create the following endpoints for data manipulation:

• GET METHOD:

``` 
endpoint: /api/v1/divise/:id
method: GET
action: Get register by id
``` 

• How to use?

  Point to their respective endpoint with the id of the object we want to fetch. Example:
  
``` 
endpoint: /api/v1/divise/:id
``` 
return: 

  
``` 
"response": {
        "id": 22,
        "usd_price": 32,
        "divise": "arg"
    },
``` 



• POST METHOD:
  
  ``` 
  endpoint: /api/v1/divise
  method: POST
  action: Create a new register in your database.
   ``` 
  
  • How to use?
  
   Once on your endpoint, create the object. Example:
  
  ``` 
    {
      "usd_price": 902,
      "divise": "arg"
    }   
  ``` 
  
 returns the created object:
 
 ``` 
 "response": {
        "id": 25,
        "usd_price": 902,
        "divise": "arg"
    }   
 ```
 
 
 • PUT METHOD:

``` 
endpoint: /api/v1/divise/:id
method: PUT
action: Update the register by id.
``` 

• How to use?

  Enter the id of the object that we want to edit. Example:
  
``` 
/api/v1/divise/:id

Object: 

"response": {
        "id": 26,
        "usd_price": 902,
        "divise": "arg"
    }
``` 

Edit and submit the request. Return the modified object:

``` 
"response": {
        "id": 27,
        "usd_price": 1004,
        "divise": "arg"
    }
 
 the object gets a new id.
``` 


 • DELETE METHOD:

``` 
endpoint: /api/v1/divise/:id
method: DELETE
action: delete the register by id.
``` 

• How to use?

Get the object to delete using the id. Example:

``` 
/api/v1/divise/:id
``` 

return: 

``` 
{
    "message": "eliminado exitosamente"
}
``` 





