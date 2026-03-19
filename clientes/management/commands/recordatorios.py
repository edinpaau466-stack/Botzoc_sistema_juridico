from django.core.management.base import BaseCommand
from clientes.models import Audiencia, Recordatorio
from django.utils import timezone
from twilio.rest import Client


def enviar_whatsapp(numero, mensaje):
    account_sid = 'AC4bbaabd025c76815329024eda570fcf7'
    auth_token = '8391a5a29470b35cef02fe0ce9504b8a'

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=mensaje,
        from_='whatsapp:+14155238886',
        to=f'whatsapp:{numero}'
    )

    print("Mensaje enviado:", message.sid)


class Command(BaseCommand):
    help = 'Verifica audiencias y crea recordatorios automáticos'

    def handle(self, *args, **kwargs):
        ahora = timezone.now()

        audiencias = Audiencia.objects.all()
        print("TOTAL AUDIENCIAS:", audiencias.count())

        print("🚀 PROBANDO ENVÍO DIRECTO")
        enviar_whatsapp("+50258253400", "🔥 PRUEBA DESDE DJANGO")

        for audiencia in audiencias:
            fecha_hora_audiencia = timezone.make_aware(
                timezone.datetime.combine(audiencia.fecha, audiencia.hora)
            )

            diferencia = fecha_hora_audiencia - ahora
            horas_restantes = diferencia.total_seconds() / 3600

            tiempos = [24, 5, 3, 1, 0.5, 0.1]

            for horas in tiempos:
                if 0 < horas_restantes <= horas:
                    existe = Recordatorio.objects.filter(
                        audiencia=audiencia,
                        horas_antes=horas
                    ).exists()

                    if not existe:
                        Recordatorio.objects.create(
                            audiencia=audiencia,
                            horas_antes=horas
                        )

                        mensaje = f"📢 Recordatorio: tienes audiencia en {horas} horas"
                        enviar_whatsapp("+50258253400", mensaje)

                        print(f"Recordatorio creado: {audiencia} ({horas}h antes)")
