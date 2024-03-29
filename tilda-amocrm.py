base_amo = 'https://******.amocrm.ru'
create_contact_url = base_amo + '/api/v4/contacts'
create_deals_url = base_amo + '/api/v4/leads'
pipeline_statuses = base_amo + '/api/v4/leads/pipelines/******/statuses'
get_custom_fields = base_amo + '/api/v4/contacts/custom_fields'
get_account = base_amo +  '/api/v4/account'
get_contact = base_amo +  '/api/v4/contacts'


@csrf_exempt
def api(request: Request) -> render:
    if request.method == 'POST':
        auth() # Checking accesses
        
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        name = request.POST.get('name', '')
        source = request.POST.get('source', '')
        
        contact_search_data  = {
            'query' : phone
            }
        
        search_contact = requests.get(
            get_contact,
            params=contact_search_data,
            headers=headers)

        params_contact = {
            'name': name,
            'first_name': name,
            'email': email,
            'custom_fields_values': [
                    {
                        'field_id': 11111,
                        'values': [
                            {
                                'value': phone
                            }
                        ]
                    }
                ]
        }
        params_deal = {
                'name': f'Тестовый лид из {source}',
                'price': 0,
                'status_id': 11111,
                'pipeline_id': 11111,
                'created_by': 0,
                'custom_fields_values': [
                    {
                        'field_id': 11111,
                        'values': [
                            {
                                'value': source
                            }
                        ]
                    }
                ]
            }

        if search_contact.status_code != 204:
            contacts_count = len(
                search_contact.json()['_embedded']['contacts'])

            if contacts_count:
                contact_id = search_contact.json()['_embedded']['contacts'][0]['id']
            else:
                response_contact = requests.post(
                    create_contact_url,
                    json=[params_contact],
                    headers=headers)
                contact_id = response_contact.json()['_embedded']['contacts'][0]['id']
        else: 
            response_contact = requests.post(
                create_contact_url,
                json=[params_contact],
                headers=headers) 
            contact_id = response_contact.json()['_embedded']['contacts'][0]['id']
            
        response_deals = requests.post(
            create_deals_url,
            json=[params_deal],
            headers=headers)
        
        deal_id = response_deals.json()['_embedded']['leads'][0]['id']

        entity_leads = f'https://fashionfactoryschool.amocrm.ru/api/v4/leads/{deal_id}/link'
        params_entity_leads = {
            'to_entity_id': contact_id,
            'to_entity_type': 'contacts'
        
        }
        response_entity_leads = requests.post(
            entity_leads,
            json=[params_entity_leads],
            headers=headers)

        return HttpResponseRedirect(
            f"https://t.me/test?start=test_{source}_{contact_id}"
    return render(request, 'api/test.html')
