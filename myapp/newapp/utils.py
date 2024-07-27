import yagmail
def send_mail_to_venue_owner(venue,customer):
    yag = yagmail.SMTP('utkarshkc7@gmail.com','xyjm cems wqfa apif')

    if venue.venue_type == 'Hall':
        content = f'Your hall {venue.hall_name} is being requested to be booked by {customer['customer_name']} from {customer['date_start']} to {customer['date_end']}\n. The customer\'s email is {customer['email']} and contact number is {customer['phone_number']}.'
        yag.send(
            to = venue.hall_email_id,
            subject = 'Request Received for Venue booking',
            contents = content
        )
    elif venue.venue_type == 'Pool':
        content = f'Your pool {venue.pool_name} is being requested to be booked by {customer['customer_name']} from {customer['date_start']} to {customer['date_end']}\n. The customer\'s email is {customer['email']} and contact number is {customer['phone_number']}.'
        yag.send(
            to = venue.pool_email_id,
            subject = 'Request Received for Venue booking',
            contents = content
        )
    elif venue.venue_type == 'Community_Hall':
        content = f'Your hall {venue.community_hall_name} is being requested to be booked by {customer['customer_name']} from {customer['date_start']} to {customer['date_end']}\n. The customer\'s email is {customer['email']} and contact number is {customer['phone_number']}.'
        yag.send(
            to = venue.community_hall_email_id,
            subject = 'Request Received for Venue booking',
            contents = content
        )
    elif venue.venue_type == 'Garden':
        content = f'Your hall {venue.garden_name} is being requested to be booked by {customer['customer_name']} from {customer['date_start']} to {customer['date_end']}\n. The customer\'s email is {customer['email']} and contact number is {customer['phone_number']}.'
        yag.send(
            to = venue.garden_email_id,
            subject = 'Request Received for Venue booking',
            contents = content
        )
    