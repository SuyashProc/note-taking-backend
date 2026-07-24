from fastapi import APIRouter, Depends, status
from typing import List

from app.dependencies.auth import get_current_user
from app.models.user import User
from app.schemas.note import NoteCreate, NoteResponse, NoteUpdate
from app.services.note_service import create_note, get_notes, get_note_by_id, update_note, delete_note


router = APIRouter(
    prefix="/notes",
    tags=["Notes"]
)

@router.get(
    "/",
    response_model=List[NoteResponse]
)
async def get_all_notes(
        current_user: User = Depends(get_current_user)
):
    return await get_notes(current_user)


@router.post(
    "/",
    response_model=NoteResponse,
    status_code=201
)
async def add_note(
        note_data: NoteCreate,
        current_user: User = Depends(get_current_user)
) :
    return await create_note(
        note_data,
        current_user
    )

@router.get(
    "/{note_id}",
    response_model=NoteResponse
)
async def get_single_note(
        note_id: int,
        current_user: User = Depends(get_current_user)
):
    return await get_note_by_id(
        note_id,
        current_user
    )



@router.patch(
    "/{note_id}",
    response_model=NoteResponse
)
async def edit_note(
    note_id: int,
    note_data: NoteUpdate,
    current_user: User = Depends(get_current_user)
):
    return await update_note(
        note_id,
        note_data,
        current_user
    )

@router.delete(
    "/{note_id}",
    status_code=status.HTTP_200_OK
)
async def remove_note(
    note_id: int,
    current_user: User = Depends(get_current_user)
):
    await delete_note(note_id, current_user)

    return {
        "message": "Note deleted successfully"
    }