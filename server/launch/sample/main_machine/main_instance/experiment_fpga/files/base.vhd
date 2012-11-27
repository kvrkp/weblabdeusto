library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_ARITH.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;

entity Untitled is
	Port (
		inicio: in std_logic;
		ck: in std_logic;
		I0: in std_logic;
		O0: out std_logic
		);
end Untitled;

architecture behavioral of Untitled is

type nombres_estados is (Q0);
signal estado: nombres_estados;
signal entrada_aux: std_logic;

begin

entrada_aux<=I0;

process(inicio, ck)
begin
if inicio='1' then
	estado<=Q0;
elsif ck='1' and ck'event then
	case estado is
		when Q0 =>
			case entrada_aux is
				when others => estado<=Q0;
			end case;
		when others => estado<=Q0;
	end case;
end if;
end process;

process(estado)
begin
case estado is
	when Q0 =>
		O0<='1';
end case;
end process;

end behavioral;