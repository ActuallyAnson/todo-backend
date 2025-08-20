from fastapi import FastAPI

app = FastAPI()

#Fake data for testing api
fake_data = [{"id": 1, "task":"Buy milk", "Completed": False},
             {"id": 2, "task":"Walk Dog", "Completed": True}]


@app.get("/")
def hello():
    return {"message": "My Todo API is working!"}

@app.get("/todos")
def get_all_todos():
    return fake_data

@app.get("/todos/{todo_id}")
def get_one_todo(todo_id: int):
    for todo in fake_data:
        if todo["id"] == todo_id:
            return todo
    return {"error": "Todo not found"}    
        


