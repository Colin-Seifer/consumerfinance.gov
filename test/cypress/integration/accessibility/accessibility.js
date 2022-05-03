import { Filter } from './accessibility-helpers';

const page = new Filter();

describe( 'Test for accessibility', () => {
  beforeEach( () => {
    cy.visit( '/about-us/racial-equity/' );
    // inject axe-core. must be done after page is loaded.
    cy.injectAxe();
  } );
  it( 'Test contrast on global header links', () => {
      /* Until Cypress implements an effective hover()
      this test will not be effective. The current issue
      is that hover is a pseudo-class and as such, can't
      be touched by any Javascript functions. Cypress
      implemented a workaround for click(), but did not
      do the same for hover because of the difficulty of
      ending the hover event. */
      page.hover_link().then( () => {
        cy.checkA11y( '.m-global-header-cta' );
      });
  } );
  it.only( 'Test for aria hidden', () => {
    cy.checkAccessibility( '.o-video-player' );
  } );
} );