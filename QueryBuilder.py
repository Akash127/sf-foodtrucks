class QueryBuilder:
    '''Class defines Query Builder object to help Build 
    Queries using various SoQL clauses'''

    def __init__(self):
        pass

    def buildSelectClause(self, fields):
        return '$select=' + ','.join(fields)

    def buildWhereClause(self, expressions, joinBy="AND"):
        clause = f' {joinBy} '.join(expressions)
        return f'$where={clause}'

    def buildOrderByClause(self, field, order="ASC"):
        return "$order=" + field + " " + order

    def buildLimitClause(self, limit):
        return f'$limit={limit}'

    def buildOffsetClause(self, offset):
        return f'$offset={offset}'
