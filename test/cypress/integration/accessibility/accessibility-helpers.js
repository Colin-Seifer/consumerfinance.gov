export class Filter{
    hover_link(){
        /* Once hover is implemented by Cypress, replace
        the current line with the line that's been commented
        out. */
        return cy.get( '.m-global-header-cta a' ).first();
        // return cy.get( '.m-global-header-cta a' ).first().hover();
    }
}