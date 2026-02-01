import argparse
import subprocess

def run_web_scan(url, plugins=None):
    command = ["web_scanner", "-u", url]
    if plugins:
        command.extend(["--plugins", plugins])
    subprocess.run(command)

def run_network_scan(target, aggressive=False):
    command = ["network_scanner", "-t", target]
    if aggressive:
        command.append("--aggressive")
    subprocess.run(command)

def run_sql_injection(url, level=None, risk=None, dbs=False):
    command = ["sql_injector", "-u", url]
    if level is not None and risk is not None:
        command.extend(["--level", str(level), "--risk", str(risk)])
    if dbs:
        command.append("--dbs")
    subprocess.run(command)

def run_xss_scan(url, payload=None):
    command = ["xss_scanner", "-u", url]
    if payload:
        command.extend(["--payload", payload])
    subprocess.run(command)

def check_ssl(url, expired=False):
    command = ["ssl_checker", "-u", url]
    if expired:
        command.append("--expired")
    subprocess.run(command)

def main():
    parser = argparse.ArgumentParser(description="PentMix: Outil de Pentest Tout-en-un")
    parser.add_argument("-u", "--url", help="URL cible pour les scans web")
    parser.add_argument("-t", "--target", help="Cible pour le scan de réseau")
    parser.add_argument("-n", "--web_scan", action="store_true", help="Lancer un scan de sécurité web")
    parser.add_argument("-m", "--network_scan", action="store_true", help="Lancer un scan de réseau")
    parser.add_argument("-s", "--sql_injection", action="store_true", help="Lancer une analyse d'injection SQL")
    parser.add_argument("-a", "--all", action="store_true", help="Exécuter un scan complet")
    parser.add_argument("-x", "--xss_scan", action="store_true", help="Effectuer un scan XSS")
    parser.add_argument("-c", "--ssl_check", action="store_true", help="Vérifier les certificats SSL/TLS")
    parser.add_argument("--plugins", help="Liste de plugins spécifiques")
    parser.add_argument("--aggressive", action="store_true", help="Scan agressif")
    parser.add_argument("--level", type=int, help="Niveau de l'analyse")
    parser.add_argument("--risk", type=int, help="Risque de l'analyse")
    parser.add_argument("--dbs", action="store_true", help="Lister les bases de données")
    parser.add_argument("--payload", help="Payload XSS spécifique")
    parser.add_argument("--expired", action="store_true", help="Vérifier si les certificats SSL/TLS sont expirés")

    args = parser.parse_args()

    if args.web_scan:
        run_web_scan(args.url, args.plugins)

    if args.network_scan:
        run_network_scan(args.target, args.aggressive)

    if args.sql_injection:
        run_sql_injection(args.url, args.level, args.risk, args.dbs)

    if args.xss_scan:
        run_xss_scan(args.url, args.payload)

    if args.ssl_check:
        check_ssl(args.url, args.expired)

    if args.all:
        run_web_scan(args.url)
        run_network_scan(args.url)
        run_sql_injection(args.url)

if __name__ == "__main__":
    main()
