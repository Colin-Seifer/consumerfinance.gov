export class Filter{
    open() {
        cy.visit( '/login/' );
    }

    login() {
        cy.get( '#id_username' ).type( 'admin' );
        cy.get( '#id_password' ).type( 'admin' );
        cy.get( 'form' ).submit();
    }

    hover_link(){
        /* Once hover is implemented by Cypress, replace
        the current line with the line that's been commented
        out. */
        return cy.get( '.m-global-header-cta a' ).first();
        // return cy.get( '.m-global-header-cta a' ).first().hover();
    }
}