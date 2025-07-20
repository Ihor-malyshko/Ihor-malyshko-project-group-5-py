def convert_to_data(results):
    """
    Convert a record to a list of its attributes for table rendering.
    """
    data = []
    for record in results:
        data.append(
            [
                record.name.value,
                record.address.value if record.address else "—",
                ", ".join(p.value for p in record.phones) if record.phones else "—",
                record.emails[0].value if record.emails else "—",
                (
                    record.birthday.value.strftime("%d.%m.%Y")
                    if record.birthday
                    else "—"
                ),
                record.note.description if record.note else "—",
                record.note.tags if record.note else "—",
            ]
        )
    return data