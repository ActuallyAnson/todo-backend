from fastapi import FastAPI

app = FastAPI()

#Fake data for testing api
fake_data = [{"ID": 1, "Task":"Buy milk", "Completed": False},
             {"ID": 2, "Task":"Walk Dog", "Completed": True}]


@app.get("/")
def hello():
    return {"message": "My Todo API is working!"}

#list todos (reading)
@app.get("/todos")
def get_all_todos():
    return fake_data

@app.get("/todos/{todo_id}")
def get_one_todo(todo_id: int):
    for todo in fake_data:
        if todo["ID"] == todo_id:
            return todo
    return {"error": "Todo not found"}


#add todos (writing)
@app.post("/todos")
def create_todo(task: str):
    # Find the highest ID and add 1: Find out why is it like this later
    if fake_data:
        new_ID = max([todo["ID"] for todo in fake_data]) + 1
    else:
        new_ID = 1
    
    new_todo = {"ID": new_ID, 
                "Task": task, 
                "Completed": False}
    fake_data.append(new_todo)
    return new_todo

