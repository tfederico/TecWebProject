#!/usr/bin/perl -w
use CGI;
use utf8;
binmode STDIN, ":encoding(utf8)";
binmode STDOUT, ":encoding(utf8)";
use Encode;
use lib './perl/modules/';
use PageSkeleton;
use HtmlFunctions;
use FilmFormControl;
print "Content-Type: text/html\n\n";

PageSkeleton::printDocType();
PageSkeleton::printHeadStart();
print
"	<script type=\"text/javascript\" src=\"../public_html/javascript/controlliInserimentoFilmInSala.js\"></script>";
my $nomePagina = "Inserisci un nuovo film in sala - Amministrazione - InstaFilm";
my $description = "Pagina per l'inserimento di un film";
my $keyword = "Film, Cinema, InstaFilm, Film in sala, inserimento film";
PageSkeleton::printHeadEnd($nomePagina, $description, $keyword);
print "<body onload=\" ridimensionamentoPagina(); caricamento();\">";
PageSkeleton::printHeader();
PageSkeleton::printNav($nomePagina);
#creazione breadcrumb
$nomeBC="<a href=\"Amministrazione.cgi\">Amministrazione</a> <span class=\"breadcrumb\">-&gt;</span> <a href=\"SceltaInserimentoFilmSala.cgi\">Inserisci film in sala</a> <span class=\"breadcrumb\">-&gt;</span> "."Inserisci un nuovo film in sala";
PageSkeleton::printBreadCrumb($nomeBC);
PageSkeleton::printLoginBar();
PageSkeleton::printContentStart();
#Qui va inserito il contenuto
#controllo sel'utente è registrato come amministratore
my $cgi = new CGI;
my $sid = $cgi->cookie('CGISESSID') || $cgi->param('CGISESSID') || undef;
my $session = load CGI::Session();
if (DBFunctions::controlAdmin($session->param("utenteEmail")) == 0){
	print "<h1>Accesso negato</h1>
		   <p>Sezione riservata solamente agli amministratori del sito web.</p>
		   <p>Se sei un amministratore devi eseguire il <a href=\"Login.cgi\">login</a> prima di poter accere.</p>";
} else {
	#recupero parametri per controllo degli errori e per risettare i campi come messo dall'utente
	my $errtitolo = $session->param("errTitolo");
	my $errpaese = $session->param("errPaese");
	my $errdurata = $session->param("errDurata");
	my $errregia = $session->param("errRegia");
	my $errattori = $session->param("errAttori");
	my $errtrama = $session->param("errTrama");
	my $errdatauscita = $session->param("errDataUscita");
	my $errrecensione = $session->param("errRecensione");
	my $errval = $session->param("errValutazione");
	my $errincasso= $session->param("errIncasso");
	my $errDescrLoc = $session->param("errDescrLoc");
	my $titolo = $session->param("titolo") || undef;
	my $paese = $session->param("paeseDiProduzione") || undef;
	my $durata = $session->param("durata") || undef;
	my $regia = $session->param("regia") || undef;
	my $attori = $session->param("attori") || undef;
	my $trama = $session->param("trama") || undef;
	my $giornoUscita = $session->param("giornoUscita") || undef;
	my $meseUscita = $session->param("meseUscita") || undef;
	my $annoUscita = $session->param("annoUscita") || undef;
	my $annoProduzione = $session->param("annoProduzione") || undef;
	my $gen = $session->param("genere") || undef;
	my $recensione = $session->param("recensione") || undef;
	my $val = $session->param("ValutazioneFilm") || undef;
	my $incasso = $session->param("incasso") || undef;
	my $locdescr = $session->param("locDescr") || undef;
	print
	"<h1>Inserisci nuovo film in sala</h1>
	<form id=\"frmInsFilm\"  method=\"post\" action=\"perl/controlloInserimentoNuovoFilmInSala.cgi\"
	 onsubmit=\"return validaForm();\">
		<fieldset>
			<legend>Inserisci dati film:</legend>";
			FilmFormControl::titolo($errtitolo, $titolo);
			print "
			<label for=\"locandina\">Inserisci il percorso o l'url della locandina:</label>
			<input type=\"text\" name=\"locandina\" id=\"locandina\" />";
			FilmFormControl::descrizione($errDescrLoc, $locdescr);
			FilmFormControl::paeseDiProduzione($errpaese, $paese);
			FilmFormControl::durata($errdurata, $durata);
			FilmFormControl::annoDiProduzione($annoProduzione);
			FilmFormControl::dataUscita($errdatauscita, $giornoUscita, $meseUscita, $annoUscita);
			FilmFormControl::incasso($errincasso, $incasso);
			FilmFormControl::regia($errregia, $regia);
			FilmFormControl::attori($errattori, $attori);
			FilmFormControl::genere($gen);
			FilmFormControl::trama($errtrama, $trama);
			FilmFormControl::recensione($errrecensione, $recensione);
			FilmFormControl::valutazione($errval, $val);
			print "
			<input type=\"submit\" value=\"Inserisci film\" />
		</fieldset>
	</form>";
}
#Fine contenuto
PageSkeleton::printContentEnd();
PageSkeleton::printFooter();
PageSkeleton::printBodyEnd();
PageSkeleton::printHtmlEnd();
