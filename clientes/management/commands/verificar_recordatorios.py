from django.core.management.base import BaseCommand
from django.utils import timezone
from clientes.models import Recordatorio
from datetime import timedelta
from twilio.rest import Client
import datetime


class Command(BaseCommand):
    help = "Verifica recordatorios de audiencias"

    def handle(self, *args, **kwargs):

        account_sid = "AC4bbaabd025c76815329024eda570fcf7"
        auth_token = "8ee2fa5ba90403710184ed3df4878f79"

        client = Client(account_sid, auth_token)

        ahora = timezone.now()

        recordatorios = Recordatorio.objects.filter(enviado=False)

        for r in recordatorios:

            audiencia = r.audiencia

            fecha_audiencia = timezone.make_aware(
                datetime.datetime.combine(
                    audiencia.fecha,
                    audiencia.hora
                )
            )

            tiempo_recordatorio = fecha_audiencia - timedelta(hours=r.horas_antes)

            print("Revisando audiencia:", audiencia.expediente)

            if ahora >= tiempo_recordatorio:

                mensaje = f"""
⚖ Recordatorio de audiencia

Expediente: {audiencia.expediente}
Fecha: {audiencia.fecha}
Hora: {audiencia.hora}

Faltan {r.horas_antes} horas.
"""

                print("Enviando WhatsApp...")

                client.messages.create(
                    body=mensaje,
                    from_="whatsapp:+14155238886",
                    to="whatsapp:+50238161244"
                )

                r.enviado = True
                r.save()

                print("Recordatorio enviado correctamente")
