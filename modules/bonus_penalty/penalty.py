from modules.bonus_penalty import bonus


def penalty_for_sales():
    if not bonus.bonus_by_sales():
        return


def penalty_for_amount():
    if not bonus.bonus_by_amount():
        return


def penalty_for_performance():
    pass
