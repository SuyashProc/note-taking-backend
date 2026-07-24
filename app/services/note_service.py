from fastapi import HTTPException, status
from app.models.note import Note
from app.models.user import User
from app.schemas.note import NoteCreate, NoteUpdate
from typing import List


async def create_note(
        note_data: NoteCreate,
        current_user: User
) -> Note:

    note = await Note.create(
        title=note_data.title,
        content=note_data.content,
        owner=current_user
    )

    return note


async def get_notes(current_user: User) -> List[Note]:
    return await Note.filter(
        owner=current_user
    ).all()

async def get_note_by_id(
    note_id: int, 
    current_user: User
    ) -> Note:

    note = await Note.get_or_none(
        id=note_id,
        owner=current_user
    )

    if note is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Note not found"
        )

    return note

async def update_note(
    note_id: int,
    note_data: NoteUpdate,
    current_user: User
) -> Note:

    note = await get_note_by_id(note_id, current_user)

    update_data = note_data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(note, field, value)

    await note.save()

    return note

async def delete_note(
    note_id: int,
    current_user: User
) -> None:

    note = await get_note_by_id(note_id, current_user)

    await note.delete()

