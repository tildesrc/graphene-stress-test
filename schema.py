import graphene

class Node(graphene.ObjectType):
    children = graphene.List(graphene.NonNull('schema.Node'), branching_factor=graphene.Int())
    value = graphene.Int(required=True)
    def resolve_children(parent, info, branching_factor):
        return [
            {'value': parent['value'] + 1}
            for _ in range(branching_factor)
        ]

class Query(graphene.ObjectType):
    root = graphene.Field(Node, required=True)
    def resolve_root(root, info):
        return {
            'value': 0
        }

schema = graphene.Schema(query=Query)
