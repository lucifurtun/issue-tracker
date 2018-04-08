def user_has_create_access(view, user):
    if user.is_superuser:
        return True

    return False


def user_has_read_access(view, user):
    if user.is_superuser:
        return True

    if user.is_staff:
        return True

    return False


def user_has_update_access(view, user):
    if user.is_superuser:
        return True

    if user.is_staff:
        return True

    return False


def user_has_delete_access(view, user):
    if user.is_superuser:
        return True

    return False
