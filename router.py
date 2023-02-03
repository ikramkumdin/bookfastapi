from fastapi import APIRouter, HTTPException, Path,Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from Schemas import BookSchema, RequestBook, Response
import crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@router.post('/create')
async def create(request:RequestBook, db:Session=Depends(get_db)):
    crud.create_book(db,book=request.parameter)
    return Response(code=200, status="ok",message="Book created successfully").dict(exclude_none=True)

@router.get("/")
async def get(db:Session=Depends(get_db)):
    _book = crud.get_book(db,0,100)
    return Response(code=200, status="0k",message="Success Fatch all data", result=_book).dict(exclude_none=True)


@router.get("/{id}")
async def get_by_id(id:int,db:Session=Depends(get_db)):
    _book = crud.get_book(db,id)
    return Response(code=200, status="0k",message="Success get data", result=_book).dict(exclude_none=True)

@router.post('/update')
async def upadate_book(request:RequestBook, db:Session=Depends(get_db)):
    _book = crud.update_book(db,book_id=request.parameter.id, title=request.parameter.title,description=request.parameter.description)
    return Response(code=200, status="ok",message="Book updated successfully",result=_book)

@router.delete("/{id}")
async def delete(id:int, db:Session = Depends(get_db)):
    crud.remove_book(db,book_id=id)
    return Response(code=200, status="ok",message="Book deleted successfully").dict(exclude_none=True)