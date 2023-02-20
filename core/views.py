from django.shortcuts import render, redirect
from django.views import View
from .models import *
from .forms import AddBookForm, AddAttributeForm, AddAttributeValueForm, BookAttributeValueForm

# Create your views here.
class Home(View):
    def get(self, request):
        book_data = Book.objects.all()
        #paginated_book_data = book_data[1: 10];
        return render(request, 'core/home.html', {'bookdata' : book_data})
        #return render(request, 'core/home.html', {'paginated_book_data' : paginated_book_data})

class Add_Book(View):
    def get(self, request):
        fm = AddBookForm()
        return render(request, 'core/add-book.html', {'form' : fm})  

    def post(self, request):
        fm = AddBookForm(request.POST)
        fmAttr = AddAttributeForm(request.POST)
        fmAttrv = AddAttributeValueForm(request.POST)
        fmBookAttrAttrv = BookAttributeValueForm(request.POST)
        
        if fm.is_valid():
            obj = fm.save()
            
            attr_count = request.POST.get('a')
            if int(attr_count) > 0:
                bookdt = Book.objects.get(id=obj.pk)            
                for i in range(1,int(attr_count)+1):
                    attr = request.POST.get('attr'+str(i))
                    attr_value = request.POST.get('attrval'+str(i))

                    att, _ = Attribute.objects.get_or_create(attribute=attr)
                    if fmAttr.is_valid():
                        fmAttr.save()
                    attv, _ = AttributeValue.objects.get_or_create(attribute_value=attr_value)
                    if fmAttrv.is_valid():    
                        fmAttrv.save()

                    BookAttributeValue.objects.get_or_create(
                        book=bookdt,
                        attribute=att,
                        attribute_value=attv
                    )
                    if fmBookAttrAttrv.is_valid():    
                        fmBookAttrAttrv.save()


            # print(request.POST)
            # print(type(attr_count))
            return redirect('/')
        else:
            return render(request, 'core/add-book.html', {'form' : fm})    

class Delete_Book(View):
    def post(self, request):
        data = request.POST
        id = data.get('id')
        studata = Book.objects.get(id=id)
        studata.delete()
        return redirect('/')

class Edit_Book(View):
    def get(self, request, id):
        bookdt = Book.objects.get(id=id)
        fm = AddBookForm(instance=bookdt)
        all_attributes = Attribute.objects.all()
        all_attributeValues = AttributeValue.objects.all()
        selected_attributes = bookdt.book_attrs.all()
        return render(request, 'core/edit-book.html', {
            'form' : fm, 
            'all_attributes': all_attributes,
            'all_attributeValues': all_attributeValues,
            'selected_attributes': selected_attributes    
        })  

    def post(self, request, id):
        bookdt = Book.objects.get(id=id)
        fm = AddBookForm(request.POST, instance=bookdt)
        attr_count = request.POST.get('attr_count')
        attr_name = request.POST.get('aan_1')
        attr_value = request.POST.get('aav_1')

        att, _ = Attribute.objects.get_or_create(attribute=attr_name)
        attv, _ = AttributeValue.objects.get_or_create(attribute_value=attr_value)
        BookAttributeValue.objects.get_or_create(
            book=bookdt,
            attribute=att,
            attribute_value=attv
        )

        if fm.is_valid():
            fm.save()
            return redirect('/')

class AttributeList(View):
    def get(self, request):
        attribute_data = Attribute.objects.all()
        return render(request, 'core/attribute.html', {'attributedata' : attribute_data})

class Add_Attribute(View):
    def get(self, request):
        fm = AddAttributeForm()
        return render(request, 'core/add-attribute.html', {'form' : fm})  

    def post(self, request):
        fm = AddAttributeForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
            return render(request, 'core/add-attribute.html', {'form' : fm})     

class Edit_Attribute(View):
    def get(self, request, id):
        attribute_data = Attribute.objects.get(id=id)
        fm = AddAttributeForm(instance=attribute_data)
        return render(request, 'core/edit-attribute.html', {'form' : fm})  

    def post(self, request, id):
        attribute_data = Attribute.objects.get(id=id)
        fm = AddAttributeForm(request.POST, instance=attribute_data)
        if fm.is_valid():
            fm.save()
            return redirect('/')         

class Delete_Attribute(View):
    def post(self, request):
        data = request.POST
        id = data.get('id')
        attribute_data = Attribute.objects.get(id=id)
        attribute_data.delete()
        return redirect('/')


class AttributeValueList(View):
    def get(self, request):
        attributevalue_data = AttributeValue.objects.all()
        return render(request, 'core/attributevalue.html', {'attributevaluedata' : attributevalue_data})

class Add_AttributeValue(View):
    def get(self, request):
        fm = AddAttributeValueForm()
        return render(request, 'core/add-attributevalue.html', {'form' : fm})  

    def post(self, request):
        fm = AddAttributeValueForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
            return render(request, 'core/add-attributevalue.html', {'form' : fm})    

class Edit_Attributevalue(View):
    def get(self, request, id):
        attributevalue_data = AttributeValue.objects.get(id=id)
        fm = AddAttributeValueForm(instance=attributevalue_data)
        return render(request, 'core/edit-attributevalue.html', {'form' : fm})  

    def post(self, request, id):
        attributevalue_data = AttributeValue.objects.get(id=id)
        fm = AddAttributeValueForm(request.POST, instance=attributevalue_data)
        if fm.is_valid():
            fm.save()
            return redirect('/')             

class Delete_Attributevalue(View):
    def post(self, request):
        data = request.POST
        id = data.get('id')
        attributevalue_data = AttributeValue.objects.get(id=id)
        attributevalue_data.delete()
        return redirect('/')            
