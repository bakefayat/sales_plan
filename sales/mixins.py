class FieldsMixin:
    def dispatch(self, request, *args, **kwargs):
        self.fields = [
            ('consumer', 'sale_plan')
        ]
        if self.request.is_superuser:
            self.fields.append('seller')
        return super().dispatch(request, *args, **kwargs)
