
jQuery.fn.dataTable.Api.register( 'sum()', function ( ) {
    return this.flatten().reduce( function ( a, b ) {
        if ( typeof a === 'string' ) {
            a = a.replace(/[^\d.-]/g, '') * 1;
        }
        if ( typeof b === 'string' ) {
            b = b.replace(/[^\d.-]/g, '') * 1;
        }
 
        return a + b;
    }, 0 );
} );

/*inicializar tabla */
$(document).ready(function(){
    var tabla = $("#example").DataTable({
           "createdRow":function(row,data,index){                   
               //pintar una celda
               if(data[5] >= 1000){
                   /* $('td', row).eq(5).css({
                       'background-color':'#ff5252',
                       'color':'white', 
                   }); */
               
                //pintar una fila
                $('td', row).css({
                       'background-color':'#5B0CBE',
                       'color':'white',
                       'border-style':'solid',
                       'border-color':'#bdbdbd' 
                   });
               }
           }, 
            "drawCallback":function(){
                  //alert("La tabla se está recargando"); 
                  var api = this.api();
                  $(api.column(5).footer()).html(
                      'Total: '+api.column(5, {page:'current'}).data().sum()
                  )
            }
    });

    //1era forma para sum()
    //var tot = tabla.column(5).data().sum();
    //$("#total").text(tot);
});



