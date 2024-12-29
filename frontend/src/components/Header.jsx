import { useLocation } from "react-router-dom";
import { navigation } from "../constants";
import Button from "./button";
import MenuSvg from "../assets/svg/MenuSvg";
import { HamburgerMenu } from "./design/Header";
import { useState } from "react";




const Header = () => {
    const [openNavigation, setOpenNavigation] = useState(true);
    const toggleNavigation = () => {
        if (openNavigation) {
          setOpenNavigation(false);
          enablePageScroll();
        } else {
          setOpenNavigation(true);
          disablePageScroll();
        }
      };
    
      const handleClick = () => {
        if (!openNavigation) return;
    
        enablePageScroll();
        setOpenNavigation(false);
      };
    return (
        <div className={`fixed top-0 left-0 w-full z-50 bg-n-11/90 backdrop-blur-sm border-b border-n-10/50 lg:bg-n-11/90 lg:backdrop-blur-sm ${openNavigation ? "bg-n-11" : "bg-n-11/90 backdrop-blur-sm" }`}>
          <div className="flex items-center px-5 lg:px-7.5 xl:px-10 max-lg:py-4">
            <a className="block w-[12rem] xl:mr-8 " href="#hero">
            <img src="../public/hh.svg" width={190} height={40} alt="Brainwave" />
            </a>
            <nav className={` ${openNavigation ? "flex" : "hidden"} fixed top-[5rem] left-0  right-0 bottom-0 bg-n-11 lg:static lg:flex lg:mx-auto lg:bg-transparent`}>
                <div className="relative z-2 flex flex-col items-center justify-center m-auto lg:flex-row">
                    {navigation.map((item) => (
                        <a 
                        key={item.id} 
                        href={item.url}
                        onClick={handleClick}
                        className={`block relative font-code txt-2xl uppercase text-n-1 transition-colors hover:text-color-1 ${item.onlyMobile ? "lg:hidden" : "" } px-6 py-6 md:py-8 lg:-mr-0.25 lg:text-xs `}
                        >
                            {item.title}
                        </a>
                    ))}
                </div>
                <HamburgerMenu />

            </nav>
            <a className="botton hidden font-code mr-8 text-n-1/50 transition-colors hover:text-n-1 lg:block" href="#signup">
                Sign in
            </a>
            <Button className="hidden lg:flex" href="#contact">
                Contact Us
            </Button>
            <Button className="ml-auto lg:hidden px-3"  onClick={toggleNavigation}>
                <MenuSvg openNavigation={openNavigation} />
            </Button>
            
          </div>
        </div>


  )
}

export default Header;
